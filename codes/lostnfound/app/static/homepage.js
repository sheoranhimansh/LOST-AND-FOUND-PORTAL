
function isNum(str) {
        return /^[0-9]+$/.test(str);
}

var colorChange = function()
{
	var phone = document.getElementById('phoneform').value;
	
	if(!isNum(document.getElementById('phoneform').value))
    	{
	    if(phone.length==0)return;
	    document.getElementById('phoneform').style.border = "2px solid red";
	    document.getElementById('phoneform').value = null;
    	}
	else
	{
	    document.getElementById('phoneform').style.border = "2px solid green";
	}
}

var splitEmail = function()
{
	var email = document.getElementById('emailform').value;
	var domain = email.split('@');
	if(domain.length==2 && domain[1].split('.').length>=2)
	{
	    document.getElementById('emailform').style.border = "2px solid green";
	}
	else
	{
	    document.getElementById('emailform').style.border = "2px solid red";
	    document.getElementById('emailform').value = null;
	}
	return;
}

var check = function()
{
	console.log('inside');
	var username = document.getElementById('usernameform').value;
	$.ajax({
		url: 'http://127.0.0.1:5000/user',
		method: 'POST',
		data: {user:username},
		success:function(response)
			{
				if(response=="True")
	    			{document.getElementById('usernameform').style.border = "2px solid green";}
				else
				{
	    				document.getElementById('usernameform').style.border = "2px solid red";
	    				document.getElementById('usernameform').value = null;
				}
			},
		error:function(response)
			{
				console.log('error');
	    			document.getElementById('usernameform').style.border = "2px solid red";
	    			document.getElementById('usernameform').value = null;
			}
		});
}

var checkLength = function()
{
	var password = document.getElementById('passwordform').value;
	if(password.length<=8)
	{
	    	document.getElementById('passwordform').style.border = "2px solid red";
	    	document.getElementById('passwordform').value = null;
	    	$('#passwordform').attr("placeholder","Use More Characters");
	}
	else
	{
	    	document.getElementById('passwordform').style.border = "2px solid green";
	}

}
