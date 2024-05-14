console.log("Script file loaded!");

document.addEventListener('DOMContentLoaded', function() {
    calculateTotal();
});

function calculateTotal() {
    var total = 0;
    var subtotalElements = document.querySelectorAll('#items-table .subtotal span');
    subtotalElements.forEach(function(element) {
        var subtotal = parseFloat(element.textContent);
        total += subtotal;
    });
    document.getElementById('total').textContent = 'Total: ' + total.toFixed(2);
}
