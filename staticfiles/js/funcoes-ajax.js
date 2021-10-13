function utilizouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    valor = document.getElementById('campo').value;
    console.log(valor);

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem)
            $("#HorasAtualizadas").text(result.horas)
        }
    });
}