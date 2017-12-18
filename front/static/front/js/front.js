/**
 * Created by rlichiere on 18/12/2017.
 */

function applicationAction(appId, envId, action) {
    console.log('applicationAction: appId:' + appId + ', envId: ' + envId + ', action: ' + action);
    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var post_data = {
        'csrfmiddlewaretoken': csrf_token,
        'command': 'application',
        'env_id': envId,
        'action': action
    };
    var url = '/api/application/' + appId + '/';
    $.post(url, post_data, function(data, status) {
        console.log('applicationAction: done, data: ' + data);
    }, 'json');
}
