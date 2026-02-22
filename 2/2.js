var a = [2,4,3];
var b = [5,6,4];

   var result = [];
    var arrtonum = function(arr){
         let num = ""; 
         arr.toString();
         for(let x of arr){
            num += x; 
         }
        return num*1;
    };
    
    var resultnum = arrtonum(a) + arrtonum(b);
    
    while(resultnum > 0){
      
       result.push(resultnum % 10);
       if(resultnum == 0) break;
       resultnum = Math.floor(resultnum / 10); 
    }

    console.log(result.reverse());