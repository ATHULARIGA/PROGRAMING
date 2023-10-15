
// function outer(){
//     let counter=0
//     function inner(){
//         counter++
//         console.log(counter )
//     }
//     inner()
// }
// outer()
function sum(a,b,c){
    return a + b + c
}

function curry(fn){
    return function (a){
        return  function (b){
            return function (c){
                return fn(a,b,c)
            }
        }
    }
}
const x=curry(sum)
console.log(x(2)(3)(5))

const add2=x(2)
const add3=add2(3)
const add4=add3(5)
console.log(add4)