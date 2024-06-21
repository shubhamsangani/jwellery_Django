$(document).ready(function(){
    console.log('helloads')
    $(document).on('change','.custom-control-input', function() {
        console.log('geadkasdf')
        if ($(this).is(':checked')) {
            var id = $(this).data('id');
            var value = $(this).data('value');
            console.log("Checkbox ID:", id);
            console.log("Checkbox Value:", value);
        }
    });
});