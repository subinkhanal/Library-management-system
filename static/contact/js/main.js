$(function() {

	'use strict';

	// Form

	var contactForm = function() {

		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					name: "required",
					email: {
						required: true,
						email: true
					},
					phone: {
						required: true,
						minlength: 10,
						maxlength: 10	
					},
					message: {
						required: true,
						minlength: 5,
					}
				},
				messages: {
					name: "Please enter your name",
					email: "Please enter a valid email address",
					message: "Please enter a message",
					phone: "Please enter a valid phone number"
				},
				submitHandler: function(form) {		
					$.ajax({   	
				      type: "POST",
				      url: "php/send-email.php",
				      data: $(form).serialize(),
				  });    		
				  alert("The form was submitted");
				  location.reload();
		  		}
			} );
		}
	};
	contactForm();

});