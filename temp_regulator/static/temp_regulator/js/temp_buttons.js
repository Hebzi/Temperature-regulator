function set_temperature(temp, sign) {
    return confirm('You\'re going to set temperature to ' + temp + sign + 'C. Are you sure?' )
}

// $(document).ready(function () {
//     $('.temp-button').click(function (e) {
//         $.ajax({
//             url: '',
//             type: 'get',
//             data: {
//                 button_class: $(this).text()
//             },
//             success: function (response) {
//                 $(".temp-button").text(response.seconds)
//             }
//         })
//
//     });
// });


$(document).ready(function () {
    $('.temp-button').click(function (e) {
        e.preventDefault()

        const temp = $(this).attr('id')
        console.log(temp)

        // const url = $(this).attr('action')
        // console.log(url)

    });
});