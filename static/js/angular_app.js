var app = angular.module('doorsApp', []);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
});

/*app.directive('goods_hover', function(){
        return function($scope, $element){
            alert('hh');
            $element.on('click',function(){
                alert('hh');
          //$(this).children().toggle();
        });
    };
});*/

app.controller('DoorsController', function($scope, $http){
    $http.get('/api/goods.json').success(function(data){
       $scope.goods = data;
    });
    $http.get('/api/actions.json').success(function(data){
       $scope.actions = data;
    });
    $scope.name = 'Boris';  
    
    $scope.doorHover = function($event){
        target = $event.target
        if (target.className.indexOf('good_card')<0)
            target = target.offsetParent;
        descfield = angular.element(target.querySelector('p'));
        console.log(target);
        console.log($event);
        console.log($scope);
        if ($event.type=="mouseover")
            descfield.removeClass('good-desc');
        else
            descfield.addClass('good-desc');            
    };
});

app.controller('ColorsController', function($scope, $http){
    $scope.showImage = function(color_id){        
        $http.get('/api/goods_images/'+color_id+'.json').success(function(data){
            $scope.mainImage = data[0].image;
        }); 
    };
});

app.directive('goodCard', function($scope){
    
});