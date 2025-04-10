

//https://datatables.net/download/index

$(document).ready(function () {
    // if request needs to be made with CSRF_TOKEN, needs to be uncommented
    // here and the headers attribute as well
    //var csrf_token = $('meta[name=csrf-token]').attr('content')

    $('#usertable').DataTable({
        processing: true,
        serverSide: true,
        searching: true,
        lengthMenu: [[10, 25, 50, 100, 200, 500], [10, 25, 50, 100, 200, 500]],
        pageLength: 10,
        ajax: {
            url: '/',
            type: 'POST',
            // If 
            // headers: {
            //   "X-CSRFToken": csrf_token,
            // },
            // success: function (result) {
            //     console.log(result)
            // },
            error: function (error_result) {
                console.log(error_result)
            },
        },
        columns: [
            { data: "id", },
            { data: "surname" },
            { data: "firstname" },
            {
                data: "age",
                //applying customization to table column values
                render: function (data, type, row, meta) {
                    if (Number(data) % 2 == 0) { //if id is even apply these to its column record
                        return '<td><span class="w-100 badge text-bg-primary">' + data + '</span></td>';
                    }
                    else if (Number(data) % 2 != 0) { //if id is odd apply these to its column record
                        return '<td><span class="w-100  badge text-bg-success">' + data + '</span></td>';
                    }
                }
            },
            { data: "phone_number" },
            { data: "address" },
        ],
    });
});
