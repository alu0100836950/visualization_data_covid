$('#btn-data-file').on('click', () => {

    let link = $('#data-file').val()
    fetch(`/dataFile`, {
        method: 'POST',
        body: JSON.stringify({'link': link}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(res => {
        res.header.forEach(key => {
            $('#data-x')
            .append($('<option></option>')
            .attr('value', key)
            .text(key))


            $('#data-y')
            .append($('<option></option>')
            .attr('value', key)
            .text(key))


            })

        if (res.date == true){
            $('#data-x').hide()
            $('#data-y').hide()

        }
        else{
            
            $('#data-x').show()
            $('#data-y').show()

        }
    })
});

$('#btn-data-file').on('click', () => {

    let link = $('#data-file').val()
    fetch(`/dataFile`, {
        method: 'POST',
        body: JSON.stringify({'link': link}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(res => {
        res.header.forEach(key => {

            $('#data-x-dis')
            .append($('<option></option>')
            .attr('value', key)
            .text(key))


            $('#data-y-dis')
            .append($('<option></option>')
            .attr('value', key)
            .text(key))

            })

        if (res.date == true){

            $('#data-x-dis').hide()
            $('#data-y-dis').hide()
        }
        else{
            
            $('#data-x-dis').show()
            $('#data-y-dis').show()
        }
    })
});

$('#type-graph').on('change', () => {
    if($('#type-graph').val() == 'box'){
        $('#data-x-dis').hide()
    }else{

    $('#data-x-dis').show()
 }
})