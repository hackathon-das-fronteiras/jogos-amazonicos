inicioQuiz = function(){
     $('#div_quiz').html('');
    $.ajax({
       url: URL_LOGGED,
       method: "GET",
       success: function (data, textStatus, jqXHR) {
            $('#div_quiz').html(data);
       }
    });
}

exec_hdata = function(el, qmodal){
    if (qmodal != '') $('#'+qmodal).modal('hide');
    $('#div_quiz').html('');
    $.get({url: $(el).attr('hdata')});
    inicioQuiz();
}

acessar = function(){
    data_send = $('#formlogin').serialize();
    $.ajax({
       url: URL_LOGIN,
       method: "POST",
       data: data_send,
       success: function (data, textStatus, jqXHR) {
            dat = jqXHR.responseText;
            if (dat == "#nodata"){
                alert(MSG_NODATA);
            }else if (dat == "#erroruser"){
                alert(MSG_ERRORLOGIN);
            }else{
                inicioQuiz();
            }
       }
    });
}

insertUser = function(){
    data_send = $('#formlogin').serialize();
    $.ajax({
       url: URL_CADLOGIN,
       method: "POST",
       data: data_send,
       success: function (data, textStatus, jqXHR) {
            dat = jqXHR.responseText;
            if (dat == "#nodata"){
                alert(MSG_NODATA);
            }else if (dat == "#erroruser"){
                alert(MSG_ERRORCADUSER);
            }else{
                inicioQuiz();
            }
       }
    });
}

pergunta = function(){
    $.ajax({
       url: URL_QUESTAO,
       method: "GET",
       success: function (data, textStatus, jqXHR) {
            $('#div_quiz').html(data);
       }
    });
}

responder = function(idresp){
    $.ajax({
       url: URL_RESPONDER+'?r='+idresp,
       method: "GET",
       success: function (data, textStatus, jqXHR) {
            $('#div_quiz').html(data);
       }
    });

}

ranking = function(){
    $.ajax({
       url: URL_RANKING,
       method: "GET",
       success: function (data, textStatus, jqXHR) {
            $('#div_quiz').html(data);
       }
    });
}