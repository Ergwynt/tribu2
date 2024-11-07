function openModal(url){
    var $ = jQuery.noConflict();
    $('#addEchoModal').load(url, function (){
        $(this).modal('show');
    });
}