var app = angular.module('doorsApp', []);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
});


app.controller('DoorsController', function($scope, $http){
    $http.get('/api/goods.json').success(function(data){
       $scope.goods = data;
    });
    $scope.name = 'Boris';  
});

app.controller('ColorsController', function($scope, $http){
    console.log($scope.mainImg);
    $scope.showImage = function(color_id){        
        $http.get('/api/goods_images/'+color_id+'.json').success(function(data){
            $scope.mainImage = data[0].image;
        }); 
    };
});

app.directive('goodCard', function($scope){
    
});