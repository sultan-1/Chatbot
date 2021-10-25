function main(){
    //Get the textarea value
    let text = $('#textArea').val();
    
    //clear the value
    $('#textArea').val("");
    //append the bubble to the chatbox
    Bubble_format('User',text);
    //send the requset to the server!
    send(text);
}

function Bubble_format(sender,text){
    let border, bubble, msg, icon;
    if(sender === 'User'){
    //User-border
    border = $('<div></div>').attr('class','User-border');
    //User-Icon
    icon = $('<img>').attr({
        'src': '../static/img/alien.png',
        'alt': 'user Icon',
        'class': 'User-Icon'
    });
    //User-Bubble
    bubble = $('<div></div>').attr('class', 'User-Bubble');
    //User-Message
    msg = $('<p></p>').attr('class', 'User-Message');
    }else{
        
        //ChatBot-border
        border = $('<div></div>').attr('class','ChatBot-border');
        //ChatBot-Icon
        icon = $('<img>').attr({
            'src': '../static/img/chatbot.png',
            'alt': 'Chatbot Icon',
            'class': 'ChatBot-Icon'
        });
    
        //ChatBot-Bubble
        bubble = $('<div></div>').attr('class', 'ChatBot-Bubble');
    
        //ChatBot-Message
        msg = $('<p></p>').attr('class', 'ChatBot-Message');
    }//end of else block

    //Persentaton!
    $('#Container #ChatBox').append(border); 
    border.append(icon);
    border.append(bubble);
    bubble.append(msg);
    msg.text(text);
  
   
    

}

function send(msg){
   msg = msg.replace('\n','');
    let query = {
       message:msg
   };
   //convert query to json 
   query = JSON.stringify(query);
   console.log($.post.getContentType);
   //send to the server!
    $.post('/ask',query,(data,status)=>{
        console.log(status);
        Bubble_format('Chatbot',data.res);
    },'json');

 
}


$(document).ready(()=>{
    
    $('#footer #Send').on('click',()=>{
        main();
       
    });

    $('#footer #textArea').keyup( ( e )=>{
        if(e.keyCode === 13){
            main();
        }
    });


    
});