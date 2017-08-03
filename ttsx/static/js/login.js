$(function(){

	var error_name = false;
	var error_password = false;

    $('.name_input').blur(function() {
        check_name_input();
    })
	function check_name_input(){
		var len = $('.name_input').val().length;
		if(len==0)
		{
			$('.name_input').next().html('账号不能为空')
			$('.name_input').next().show();
			error_name = true;
		}
		else
		{
			$('.name_input').next().hide();
			error_name = false;
		}
	}

	$('.pass_input').blur(function() {
        check_pass_input();
    })
	function check_pass_input(){
		var len = $('.pass_input').val().length;
		if(len==0)
		{
			$('.pass_input').next().html('密码不能为空')
			$('.pass_input').next().show();
			error_password = true;
		}
		else
		{
			$('.pass_input').next().hide();
			error_password = false;
		}
	}
        $('#reg_form').submit(function() {
            check_name_input();
            check_pass_input();

		if(error_name == false && error_password == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});
	})