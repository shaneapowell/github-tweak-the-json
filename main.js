
//  Input Values are in a SPECIFIC order.
//  main.js <action> <file> <path> <value>
//  <action> = [read/write]
//  <file> = the filename
//  <path> = the dot notation path to read/write
//  <value> = the value to write , only for write mode. Ignored for read mode

const fs = require('fs')

/*
 * A simple nested json setter using dotted notation 
 */
function set(obj, path, value) {
    var schema = obj;  // a moving reference to internal objects within obj
    var pList = path.split('.');
    var len = pList.length;
    for(var i = 0; i < len-1; i++) {
        var elem = pList[i];
        if( !schema[elem] ) schema[elem] = {}
        schema = schema[elem];
    }

    schema[pList[len-1]] = value;
}


/*
 * The Main 
 */
function main() {
    args = process.argv.slice(2)
    mode = args[0]
    file = args[1]
    path = args[2]
    value = args[3] || null

    console.log(args)

    /* Try to read the json file, if it's not there, we'll start with a blank */
    var data
    try {
        let rawJson = fs.readFileSync(file)
        data = JSON.parse(rawJson)
    } catch (e) {
        data = {}
    }

    /* eval() read the dotted notation field */
    if (mode == 'read') {
        try {
            cmd = "data." + path
            value = eval(cmd)
        } catch(e) {
            value = null
        }
        console.log("::set-output name=value::" + value)
    } 

    /* Set the value, and write the file */
    if (mode == 'write') {
        set(data, path, value)
        fs.writeFileSync(file, JSON.stringify(data, null, 2))
    }

}


main()


