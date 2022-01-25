function update_used_toggle(pk, token) {
     $.ajax({
        type: 'POST',
        url: '/hora-extra/toggle/' + pk + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(JSON.stringify(result))
            update_label_used_toggle(result.value)
            $("#messagem").text("Foi marcada como usada com sucesso!");
        }
    })
}

function update_label_used_toggle(is_used) {
    let value = "Marcar como utilizada"
    if(!!JSON.parse(String(is_used).toLowerCase())){
        value = "Marcar como não utilizada"
    }
    $("#used_toggle").text(value)
}

$(document).ready(function(){
    let is_used = $("#used_toggle")
    console.log(is_used.attr("my-value"))
    update_label_used_toggle(is_used.attr("my-value"))
})