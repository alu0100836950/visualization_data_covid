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
