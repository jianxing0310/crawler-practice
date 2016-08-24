function doFirst(){
	var latlng = new google.maps.LatLng(25.026158,121.542709);
	var area = document.getElementById('message');
	var option = {
		zoom:14,
		center:latlng,
		mapTypeId:google.maps.MapTypeId.ROADMAP
	};
	
	var map = new google.maps.Map(area, option);
	var marker = new google.maps.Marker({
		position:latlng,
		map:map,
		title:'這不是我家'
	});
}
window.addEventListener('load', doFirst, false);