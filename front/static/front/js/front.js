/**
 * Created by rlichiere on 18/12/2017.
 */

function applicationAction(appName, envName, action) {
    console.log('applicationAction: app:' + appName + ', env: ' + envName + ', action: ' + action);
    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var post_data = {
        'csrfmiddlewaretoken': csrf_token,
        'command': 'application',
        'application': appName,
        'environment': envName,
        'action': action
    };
    var url = '{% url "application-api" %}';
    $.post(url, post_data, function(data, status) {
        console.log('applicationAction: done, data: ' + data);
    }, 'json');
}
