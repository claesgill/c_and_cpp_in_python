const ffi = require("ffi");

// Other imports are similar as this:
const clib = ffi.Library("./c/main.so", {
    hello: ["void", []],
    sum: ["int", ["int", "int"]]
})

clib.hello();
console.log(clib.sum(4, 5));