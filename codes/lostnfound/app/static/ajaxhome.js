var create = function(){
var firstname = $('#formfirst').val();
var lastname = $('#formlast').val();
var phone = $('#phoneform').val();
var email = $('#emailform').val();
var username = $('#usernameform').val();
var password = $('#passwordform').val();
console.log(firstname);
var country = document.getElementById('countryform');
var counval = country.options[country.selectedIndex].text;
var date = document.getElementById('dateform');
var dateval = date.options[date.selectedIndex].text;
var month = document.getElementById('monthform');
var monthval = month.options[month.selectedIndex].text;
var year = document.getElementById('yearform');
var yearval = year.options[year.selectedIndex].text;
var gender = $("input:radio[name=gender]:checked").val();
var suc = document.getElementById('success');
var fai = document.getElementById('failure');
	$.ajax({
		url:'http://127.0.0.1:5000/addUser',
		method:'POST',
		data:{first_name:firstname,last_name:lastname,username:username,password:password,gender:gender,country:counval,mobile:phone,email:email,date:dateval,month:monthval,year:yearval},
		success:function(response)
		{
			suc.style.display="block";
			setTimeout(function(){suc.style.display="none";},5000);
		},
		error:function(response)
		{
			console.log(response);
			fai.style.display="block";
			setTimeout(function(){fai.style.display="none";},5000);
		},
});};

var login = function(){
var email = $('#email').val();
var pass = $('#pass').val();
console.log('outside ajax');
	$.ajax({
		url:"http://127.0.0.1:5000/login",
		method:"POST",
		data:{email:email,password:pass},
		success:function(response)
			{
				console.log('success');
				window.location = "http://127.0.0.1:5000/dash";
	//			document.write(response);
			},
		error:function(response){},
});};
