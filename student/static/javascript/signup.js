document.getElementById("form5").addEventListener("submit", function (event)  {
    signinstatus = 1;

    //firstname validation

    fname = document.getElementById("name")

    if (fname.value == "") {
        fname.style.borderColor = "#FF0000";
        signinstatus = 0;
        event.preventDefault()


    } else {
        fname.style.borderColor = "#ced4da";
    }
    // validate id

    // rid = document.getElementById("rollid")

    // if (rid.value == "") {
    //     rid.style.borderColor = '#FF0000'; 
    //     signinstatus = 0;
    //     event.preventDefault()

    // } else {

    //     rid.style.borderColor = '#ced4da';
    // }

    // //validate date of birth

    // dateofbirth = document.getElementById("dofb")

    // if (dateofbirth.value == "") {
    //     dateofbirth.style.borderColor = '#FF0000';
    //     signinstatus = 0;
    //     event.preventDefault()

    // } else {

    //     dateofbirth.style.borderColor = '#ced4da';

    // }



    // // validate class

    // cla = document.getElementById("class");

    // if (cla.value == "") {
    //     cla.style.borderColor = "#FF0000";
    //     signinstatus = 0;
    //     event.preventDefault()

    // } else {

    //     cla.style.borderColor = "#ced4da";

    // }

    // // validate section

    // section = document.getElementById("section")

    // if (section.value == "") {
    //     section.style.borderColor = "#FF0000";

    //     signinstatus = 0;
    //     event.preventDefault()

    // }
    // else {

    //     section.style.borderColor = "#ced4da";

    // }

    // // validate year

    // year = document.getElementById("year")

    // if (year.value == "") {
    //     year.style.borderColor = "#FF0000";

    //     signinstatus = 0;
    //     event.preventDefault()

    // }
    // else {

    //     year.style.borderColor = "#ced4da";

    // }

    // // validate mobile number

    // var phoneformat = /^\d{10}$/;

    // phone = document.getElementById("userMobile");

    // if (phone.value.match(phoneformat)) {
    //     phone.style.borderColor = "#ced4da";

    // } else {

    //     phone.style.borderColor = "#FF0000";
    //     signinstatus = 0;
    //     event.preventDefault()

    // }

    // // Validate mail valid or not

    // var mailformat = /^[a-zA-Z0-9. !#$%&* +/=?^_` {|}~~]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;

    // mail = document.getElementById("semail")
    // if (mail.value.match(mailformat)) {
    //     mail.style.borderColor = "#ced4da";

    // } else {

    //     mail.style.borderColor = "#FF0000";
    //     signinstatus = 0;
    //     event.preventDefault()

    // }

    // // validate password is entered or not

    // password = document.getElementById("password");
    // cpassword = document.getElementById("cpassword");
    // document.getElementById("error").innerHTML = ""

    // if (password.value == "") {
    //     password.style.borderColor = "#FF0000";
    //     signinstatus = 0;
    //     event.preventDefault()

    // } else {

    //     password.style.borderColor = "#ced4da";

    // }
    // if (password.value != cpassword.value) {

    //     signinstatus = 0;
    //     event.preventDefault()

    //     document.getElementById("error").innerHTML = "password and confirm password mismatch";
    //     cpassword.style.borderColor = "#FF0000";

    // } else {

    //     cpassword.style.borderColor = "#ced4da";

    // }

    if (signinstatus == 0) {

        return false;

    }

})




