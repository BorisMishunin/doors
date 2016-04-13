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
    
    $scope.filters = [];
    
    $http.get('/api/properties.json').success(function(data){
       $scope.filters = data;
    });
    
    $http.get('/api/goods_colors.json').success(function(data){
       $scope.colors = data;
    });
    
    var filter = {};
    filter.name = 'Цвета';
    filter.property_values = [];
    _.each($scope.colors, function(color){
        filter.property_values.push({
            value: color.color 
        });
    });
    
    $scope.filters.push(filter);
    
    console.log($scope.filters);
    
    $scope.doorHover = function($event){
        target = $event.target
        if (target.className.indexOf('good_card')<0)
            target = target.offsetParent;
        descfield = angular.element(target.querySelector('p'));
        if ($event.type=="mouseover")
            descfield.removeClass('good-desc');
        else
            descfield.addClass('good-desc');            
    };
     $scope.ff = function(){
         console.log($scope.Filter);
     };
    
});

app.filter('GoodsFilter', function(){
    return function(goods, filters, scope){
        var filtered = [];
        
        var include_filters = _.filter(filters, function(filter){
            return _.any(filter.property_values, {'IsIncluded':true})
        });
        
        _.each(goods, function(good){
            var is_included = true;
            _.each(include_filters, function(filter){
                var properties = _.filter(good.properties, {'name': filter.name}); 
                if(! _.any(properties, function(prop){return _.any(filter.property_values, {'value': prop.value, 'IsIncluded':true});})){
                    is_included = false;
                };
            });
            if (is_included){
                filtered.push(good);
            }
        });
        return filtered;
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