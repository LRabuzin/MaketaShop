$(document).ready(function(){

    $("#showText1").click(function (){
        $('#text1').show();
        $('#showText1').hide();
    });

    $("#showMedia1").click(function (){
        $('#media1').show();
        $('#showMedia1').hide();
        $('#btnBlock2').show();
    });

    $("#hideText1").click(function (){
        $('#text1').hide();
        $('#textInput1').val('');
        $('#showText1').show();
    });

    $("#hideMedia1").click(function () {
        $('#media1').hide();
        $('#mediaInput1').val('');
        $('#showMedia1').show();
        $('#btnBlock2').hide();
    })

    $("#showText2").click(function (){
        $('#text2').show();
        $('#showText2').hide();
    });

    $("#showMedia2").click(function (){
        $('#media2').show();
        $('#showMedia2').hide();
        $('#btnBlock3').show();
    });

    $("#hideText2").click(function (){
        $('#text2').hide();
        $('#textInput2').val('');
        $('#showText2').show();
    });

    $("#hideMedia2").click(function () {
        $('#media2').hide();
        $('#mediaInput2').val('');
        $('#showMedia2').show();
        $('#btnBlock3').hide();
    })

    $("#showText3").click(function (){
        $('#text3').show();
        $('#showText3').hide();
    });

    $("#showMedia3").click(function (){
        $('#media3').show();
        $('#showMedia3').hide();
        $('#btnBlock4').show();
    });

    $("#hideText3").click(function (){
        $('#text3').hide();
        $('#textInput3').val('');
        $('#showText3').show();
    });

    $("#hideMedia3").click(function () {
        $('#media3').hide();
        $('#mediaInput3').val('');
        $('#showMedia3').show();
        $('#btnBlock4').hide();
    })

    $("#showText4").click(function (){
        $('#text4').show();
        $('#showText4').hide();
    });

    $("#showMedia4").click(function (){
        $('#media4').show();
        $('#showMedia4').hide();
        $('#btnBlock5').show();
    });

    $("#hideText4").click(function (){
        $('#text4').hide();
        $('#textInput4').val('');
        $('#showText4').show();
    });

    $("#hideMedia4").click(function () {
        $('#media4').hide();
        $('#mediaInput4').val('');
        $('#showMedia4').show();
        $('#btnBlock5').hide();
    })

    $("#showText5").click(function (){
        $('#text5').show();
        $('#showText5').hide();
    });

    $("#hideText5").click(function (){
        $('#text5').hide();
        $('#textInput5').val('');
        $('#showText5').show();
    });

});