function pick_and_set(item){
            
    for (let i = 0; i < item.length; i++) {
        j = i +1;
        col1 = document.getElementById('h'+j)
        col2 = document.getElementById('r'+j)
        if (item[i][0] == "1") {
            col1.innerHTML= "😎"
        }

        if (item[i][1] == "1") {
            col2.innerHTML= "🤖";
        }
    } 

}