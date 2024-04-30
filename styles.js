function ownervalidation(){
    var owner=document.getElementById("cardowner").value;
    if (owner.length<10){
    return false;
    }else{
return true;
    }
    }

    function cvvvalidation(){
var cvv=document.getElementById("cvv").value;
if (cvv.length !==3){
return false;
}else{
return true;
}
}

function cardnumbervalidation(){
    var cardnumber=document.getElementById("cn").value;
    if (cardnumber.length !==6){
    return false;
    }else{
    return true;
    }
    }
    function formvalidation(){
        if(!ownervalidation()){  
            alert("Enter atleast 10 characters for the card owner's naame");
        }
        if(!cvvvalidation()){
            alert("Enter  correct 3-digit CVV number");
        }
        if(!cardnumbervalidation()){
            alert("Enter a valid 6-digit card number");
        }
        if(!ownervalidation() && cvvvalidation() && cardnumbervalidation()){
            alert("Payment Successful");
        }
        else
        alert("form submitted successfully");
    
}
