function adddata(){
    var table=document.getElementById("idtable");
    //console.log("success");
    var length=table.rows.length;
    var newrow=table.insertRow(length);
    var namecol=newrow.insertCell(0);
    var phonecol=newrow.insertCell(1);
    var actioncol=newrow.insertCell(2);
    //console.log(newrow);
    namecol.innerHTML = "未命名";
    phonecol.innerHTML = '无联系方式';
    actioncol.innerHTML = '<button>编辑</button><button>删除</button>';
  
}
