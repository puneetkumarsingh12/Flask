function Test_Case1()
{
    var user_1=document.getElementById("A").value
    var pass_1=document.getElementById("B").value
    if(user_1==""||user_1==null)
    {
        document.getElementById("AAA").innerHTML="*** USERNAME IS REQUIRED ****"
        return false
    }
    else if(pass_1==""||pass_1==null)
    {
        document.getElementById("BBB").innerHTML="*** PASSWORD IS REQUIRED ***"
        return false
    }
}

