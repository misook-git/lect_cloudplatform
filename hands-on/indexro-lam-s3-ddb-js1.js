const AWS = require('aws-sdk')
const s3 = new AWS.S3()
const documentClient = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
	const {name} = event.Records[0].s3.bucket;
	const {key} = event.Records[0].s3.object;

	const getParms = {
		Bucket: name,
		Key: key
	};

  	try {
       	//var origimage = await s3.getObject(params).promise();
        const s3Data = await s3.getObject(getParms).promise();
        const usersStr = s3Data.Body.toString();
        const usersJSON = JSON.parse(usersStr);
        console.log('Users ::: ${usersStr}');

        const {id, firstname, lastname} = usersJSON[0];

        const putParams = {
        	TableName: "roddbtable1",
        	Item: {
        		id: id,
        		firstname: firstname,
        		lastname: lastname
        	}
        };

        const putItemData = await documentClient.put(putParams).promise();
		
        console.log(putItemData);
        

    	} catch (err) {
    	console.log(err);
       
    	}  
    //return;
	};