    // document.getElementById('men').onclick = (()=>{
    //     alert('MEn is clicked')

    // }) 

    //BEST APPROCH
    // document.getElementById('images').addEventListener('click', (e)=>{
    // console.log('Clicked inside the ul');

    // },)
    // document.getElementById('men').addEventListener('click', (e)=>{
    // console.log('Men Clicked ');
    // e.stopPropagation() //Event bubble hoke uper ke element pr nhi jyegaa...
    // },)

    // //EVENT PROPOGATION 
    // // there are 2 contaxt of event propogation 1. Event bubbling //bottom to top 2. Event capturing//top to bottom
    // document.getElementById('google').addEventListener
    // ('click',(e)=>{
    //     e.preventDefault();
    //     e.stopPropagation()
    //     console.log('google clicked');
    // },false)

    document.querySelector('#images').addEventListener('click' , (e)=>{
        console.log(e.target.tagName);
        if (e.target.tagName === 'IMG') {
            console.log(e.target.id);
            
            let removeIt = e.target.parentNode;
            removeIt.remove();
            
        }
        
    })