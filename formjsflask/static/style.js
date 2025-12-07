const password = document.querySelector('#password');
const username = document.querySelector('#username');
const email = document.querySelector('#email');
const form = document.querySelector('form');


form.addEventListener('submit', (e) => {
   let submitForm = true;


   if (!username.value ){
       console.log('O username está vazio')
       alert('O username está vazio')
       let submitForm = false;
   }
   if(!email.value){
       console.log('O email está vazio')
       alert(('O email está vazio'))
       let submitForm = false;
   }
   if(!password.value){
       console.log("A senha está vazia")
       alert("A senha está vazia")
       let submitForm = false;
   }
   if(!submitForm){
       e.preventDefault();
   }
  
});












// function Conferir(){
//    if ('password' = ''){
//        alert ('Insira uma senha correta')
//    }
//}








