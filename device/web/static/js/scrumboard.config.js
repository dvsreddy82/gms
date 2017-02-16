(function () {
    'use strict';

    angular.module('gdm.home')
        .config(['$routeProvider', config])
        .run(['$http', run]);

    function config($routeProvider) {

        $routeProvider
            .when('/', {
                templateUrl: '/static/html/scrumboard.html',
                controller: 'ScrumboardController'
            })
            .when('/login', {
                templateUrl: '/static/html/login.html',
                controller: 'LoginController'
            })
            .otherwise('/');
    }


    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    };
})();

