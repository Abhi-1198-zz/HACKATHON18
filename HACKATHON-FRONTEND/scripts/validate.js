// <script type="text/javascript">
console.log("success");
  (function ($, W, document)
  {
  var JQUERY4U = {};
  JQUERY4U.UTIL =
      {
          setupFormValidation: function ()
          {
          //form validation rules
          $("#empdet").validate({
              rules: {
              FNAME: "required",
              LNAME: "required",
              PHONE: {
                      required: true,
                       minlength: 10,
                       pattern: [/^[7-9]{1}[0-9]{9}$/], 
                  },
              GENDER:"required",
              DOB:"required",
              DOJ:"required",
              EMAIL: {
                      required: true,
                      email: true
                  },
              ADDRESS:"required",
              messages: {
              FNAME: "Please Enter First Name",
              LNAME: "Please Enter Last Name",
              PHONE: "Please Enter Valid Mobile Number",
              EMAIL: "Please Enter valid Email",
              DOB:"Enter your Date Of birth",
              DOJ:"Enter your Date Of joining",
              GENDER:"Enter Your Gender",
              ADDRESS:"Enter your Address",
              },
              submitHandler: function (form) {
              form.submit();
              }
          }
        }
        )}
        }
//when the dom has loaded setup form validation rules
$(document).ready(function ($) {
      JQUERY4U.UTIL.setupFormValidation();
  });
  })(jQuery, window, document);