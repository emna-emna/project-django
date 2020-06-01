function delete_confirm(id_produit)
{
    if(confirm("Voulez_vous vraiment supprimer cette facture ?"))
    {
        alert('Suppression effectuée');
        location.href="{% url 'cart:cart_remove' produit.id%}";
    }
    else
    {
        alert('Suppression annulée');
    }
}
(function() {
    'use strict';
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
})();