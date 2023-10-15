function Person(fname,lname){
    this.firstname=fname
    this.lastname=lname
}
Person.prototype.getfullname =function(){
    return this.firstname + " " + this.lastname
}
function superhero(){
    Person.call(this,fname,lname ) 
    this.issuperhero=true
}
superhero.prototype.fightcrime =function(){
    console.log('fighting crime')
}
const Batman= new  superhero('bruce','wayne')
console.log(Batman.getfullname())
superhero.prototype.constructor =superhero
console.log(batman.getfullname())