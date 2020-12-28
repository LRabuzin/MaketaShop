$(document).ready(function(){

    $("#showText1").click(function (){
        $('#text1').show();
        $('#textInput1').removeAttr('readonly');
        $('#showText1').hide();
    });

    $("#showMedia1").click(function (){
        $('#media1').show();
        $('#mediaInput1').removeAttr('readonly');
        $('#showMedia1').hide();
        $('#btnBlock2-2').show();
        $('#btnBlock2').show();
    });

    $("#hideText1").click(function (){
        $('#text1').hide();
        $('#textInput1').attr('readonly','True');
        $('#textInput1').val('');
        $('#showText1').show();
    });

    $("#hideMedia1").click(function () {
        $('#media1').hide();
        $('#mediaInput1').val('');
        $('#mediaInput1').attr('readonly','True');
        $('#showMedia1').show();
        $('#btnBlock2').hide();
        $('#btnBlock2-2').hide();
    })

    $("#showText2").click(function (){
        $('#text2').show();
        $('#textInput2').removeAttr('readonly');
        $('#showText2').hide();
    });

    $("#showMedia2").click(function (){
        $('#media2').show();
        $('#mediaInput2').removeAttr('readonly');
        $('#showMedia2').hide();
        $('#btnBlock3').show();
        $('#btnBlock3-2').show();
    });

    $("#hideText2").click(function (){
        $('#text2').hide();
        $('#textInput2').attr('readonly','True');
        $('#textInput2').val('');
        $('#showText2').show();
    });

    $("#hideMedia2").click(function () {
        $('#media2').hide();
        $('#mediaInput2').attr('readonly','True');
        $('#mediaInput2').val('');
        $('#showMedia2').show();
        $('#btnBlock3').hide();
        $('#btnBlock3-2').hide();
    })

    $("#showText3").click(function (){
        $('#text3').show();
        $('#textInput3').removeAttr('readonly');
        $('#showText3').hide();
    });

    $("#showMedia3").click(function (){
        $('#media3').show();
        $('#mediaInput3').removeAttr('readonly');
        $('#showMedia3').hide();
        $('#btnBlock4').show();
        $('#btnBlock4-2').show();
    });

    $("#hideText3").click(function (){
        $('#text3').hide();
        $('#textInput3').attr('readonly','True');
        $('#textInput3').val('');
        $('#showText3').show();
    });

    $("#hideMedia3").click(function () {
        $('#media3').hide();
        $('#mediaInput3').attr('readonly','True');
        $('#mediaInput3').val('');
        $('#showMedia3').show();
        $('#btnBlock4').hide();
        $('#btnBlock4-2').hide();
    })

    $("#showText4").click(function (){
        $('#text4').show();
        $('#textInput4').removeAttr('readonly');
        $('#showText4').hide();
    });

    $("#showMedia4").click(function (){
        $('#media4').show();
        $('#mediaInput4').removeAttr('readonly');
        $('#showMedia4').hide();
        $('#btnBlock5').show();
    });

    $("#hideText4").click(function (){
        $('#text4').hide();
        $('#textInput4').attr('readonly','True');
        $('#textInput4').val('');
        $('#showText4').show();
    });

    $("#hideMedia4").click(function () {
        $('#media4').hide();
        $('#mediaInput4').attr('readonly','True');
        $('#mediaInput4').val('');
        $('#showMedia4').show();
        $('#btnBlock5').hide();
    })

    $("#showText5").click(function (){
        $('#text5').show();
        $('#textInput5').removeAttr('readonly');
        $('#showText5').hide();
    });

    $("#hideText5").click(function (){
        $('#text5').hide();
        $('#textInput5').attr('readonly','True');
        $('#textInput5').val('');
        $('#showText5').show();
    });

});
