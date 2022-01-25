function mark_used(pk, token){
    $.ajax({
        type: 'POST',
        url:'/hora-extra/used/' + pk + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            $("#messagem").text("Foi marcada como usada com sucesso!")
        }
    })
}