jQuery(document).ready(function($) {
	var validNavigation = false;

	var url_string = window.location.href;
	var url = new URL(url_string);
	var ts = url.searchParams.get("ts");
	console.log(ts);
	if(ts==1) {
		jQuery('.eapp-popup-layout-variation-modal-component').addClass('active');
	}

	var cache_status = statusHtmlStorage('cache_nb_popup');
	var data = '';
	if (cache_status == 1) {
		data = localStorage.getItem('cache_nb_popup');
	}
	if(data!='sent_data') {
		setTimeout(function(){
			jQuery('.eapp-popup-layout-variation-modal-component').addClass('active');
		}, 25000);
	}

	if($('#nb-popup-root').length>0) {
		var folder = $('#nb-popup-root').attr('rel');
		if (folder!='' && typeof folder !== 'undefined') {
			$.ajax({
				url: "http://netbaseteam.com/popup/generate.php",
				type: "post",
				dataType:"html",
				data: {
					folder: folder
				},
				success : function (result){
					$('#nb-popup-root').html(result);
					// console.log(result);
				}
			});
		}
	}

	window.addEventListener('scroll', function (e) {
	// removeHtmlStorage('cache_nb_popup_time');
	

	// window.addEventListener('beforeunload', (event) => {
	// 	window.onbeforeunload = null;
	// 	var cache_status = statusHtmlStorage('cache_nb_popup');
	// 	var data = '';
	// 	if (cache_status == 1) {
	// 		data = localStorage.getItem('cache_nb_popup');
	// 	}
	// 	console.log(validNavigation);
	// 	if(!validNavigation && data!='sent_data') {
	// 		if (event) {
	// 			setTimeout(function(){
	// 				jQuery('.eapp-popup-layout-variation-modal-component').addClass('active');
	// 			}, 1000);
	// 			event.returnValue = 'Are you sure you want to leave?';	
	// 		}
	// 	}
	// });
});

	$('body').on('click', '.eapp-popup-control-close-component', function(event) {
		var data = 'sent_data';
	setHtmlStorage('cache_nb_popup', data, 604800); // Set Cache (7 day)
	$(this).parents('.eapp-popup-layout-variation-modal-component').removeClass('active');
});

	$('body').on('click', '.eapp-popup-button-component-2', function(event) {
		event.preventDefault();
		var popup = $(this).parents('.eapp-popup-layout-variation-modal-component');
		var form = $(this).parents('form#frm-nb');
		var name = form.find('input[name="nb-name"]').val();
		var email = form.find('input[name="nb-email"]').val();
		var message = form.find('textarea[name="nb-message"]').val();
		var check = true;
		$('.eapp-popup-block-variation-form-field-input').each(function(index, el) {
			if($(this).val()=='') {
				$(this).css('border-color', 'red');
				if (check) {
					check = false;
				}
			} else {
				if(!ValidateEmail(email)) {
					form.find('input[name="nb-email"]').css('border-color', 'red');
					if (check) {
						check = false;
					}
				} else {
					$(this).css('border-color', 'rgba(17,17,17,0.1)');
				}
			}
		});
		if (check) {
			var ref_url = $('#nb-popup-root').attr('ref-url');
			var rf_url = '';
			if (ref_url!='' && typeof ref_url !== 'undefined') {
				rf_url = ref_url;
			}
			form.css({
				'pointer-events': 'none'
			});
			form.find('.eapp-popup-button-component-2').text('Processing . . .');
			$.ajax({
				url: "http://netbaseteam.com/popup/generate.php",
				type: "post",
				dataType:"html",
				data: {
					name: name,
					email: email,
					message: message,
					ref_url: rf_url
				},
				success : function (result){
					var data = 'sent_data';
    			setHtmlStorage('cache_nb_popup', data, 604800); // Set Cache (7 day)
    			$('#nb-popup-root').html(result);
    			$('.eapp-popup-layout-variation-modal-component').addClass('active');
    		}
    	});
		} else {
			alert('Please enter information!');
		}
	});

	function changeConfirmReload() {
		window.onbeforeunload = null;
		if (confirm('Wait, do you want to receive a discount off the product?\nClick cancel and fill out our form')) {
			location.reload();
		}
	}

	function ValidateEmail(email)
	{
		var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		if(email.match(mailformat))
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	function removeHtmlStorage(name) {
		localStorage.removeItem(name);
		localStorage.removeItem(name+'_time');
	}

	function setHtmlStorage(name, value, expires) {

    if (expires==undefined || expires=='null') { var expires = 3600; } // default: 1h

    var date = new Date();
    var schedule = Math.round((date.setSeconds(date.getSeconds()+expires))/1000);

    localStorage.setItem(name, value);
    localStorage.setItem(name+'_time', schedule);
}

function statusHtmlStorage(name) {
	var date = new Date();
	var current = Math.round(+date/1000);

    // Get Schedule
    var stored_time = localStorage.getItem(name+'_time');
    if (stored_time==undefined || stored_time=='null') { var stored_time = 0; }

    // Expired
    if (stored_time < current) {
        // Remove
        removeHtmlStorage(name);
        return 0;
    } else {
    	return 1;
    }
}
});