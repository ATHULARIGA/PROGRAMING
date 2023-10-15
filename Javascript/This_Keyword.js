//implicit binding rule
const person ={
    name: "vishwas",
    saymyname:function(){
        console.log('My name is ${this.name}');
    },
}
// person.saymyname()
//person.saymyname

//Explicit binding rule
function saymyname1(){
    console.log('My name is ${this.name}')
}
saymyname1.call(person)


function person1(name){
    //this ={}
    this.name
}

const p1= new Person1('Athul')
const p2= new Person1('Batman')

console.log(p1.name,p2.name)