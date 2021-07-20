exports.handler = async (event,context,callback) => {
    // TODO implement
    const operation = event.httpMethod;
    switch (operation) {
        case 'GET':
            let data = {
                'id': 1,
                'name': '철우'
            }
            callback(null,{
                'statusCode':200,
                'headers': {},
                'body': JSON.stringify(data)
            });
            
            // code
            break;
        case 'POST':
            let data2 = {
                'id': 2,
                'name': 'postMessage:'
            }
            callback(null,{
                'statusCode': 200,
                'headers': {},
                'body': JSON.stringify(data2)
            });
            break;
        default:
            //callback(new Error('Operation Error "${operation}"'))
            // code
            callback(null,{
                'statusCode': 200
            });
    }
};