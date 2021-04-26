$(window).on('load', function() {
  document.getElementById('news_list_view').style.display = 'none'
})

let gridBtn = document.getElementById('grid_button')
let gridView = document.getElementById('news_grid_view')

let listBtn = document.getElementById('list_button')
let listView = document.getElementById('news_list_view')



gridBtn.addEventListener('click', function(){
  console.log('Grid button clicked')
  listView.style.display = 'none'
  gridView.style.display = 'block'
})


listBtn.addEventListener('click', function(){
  console.log('List button clicked')
  listView.style.display = 'block'
  gridView.style.display = 'none'
})
