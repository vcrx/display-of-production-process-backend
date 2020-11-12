$(document).ready(function () {
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    jQuery('[data-toggle="popover"], .js-popover').popover({
        container: 'body',
        animation: true,
        trigger: 'hover'
    });
});


function changeUrlParams(params) {
    let keys = Object.keys(params);
    let url = location.origin + location.pathname;
    for (let i = 0; i < keys.length; i++) {
        if (i === 0) {
            url = url + "?"
        }
        url = url + keys[i] + "=" + params[keys[i]];
        if (i !== keys.length - 1) {
            url = url + "&";
        }
    }
    location.href = url;
}

function clearUrlParams() {
    let url = location.origin + location.pathname;
    location.href = url;
}
