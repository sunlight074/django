let severity = null
let person = null
let assignee_value = null
let reporter_value = null
let app_value = null
let jobPk = null

function showSeverity(severity) {
  switch(severity){
    case 'Low' : return (`
    <div>
      <div class="flex items-center space-x-2">
      <div class="h-5 w-5 rounded-full bg-green-700"></div>
      <div>Low</div>
      </div>
    </div>
    `);
    case 'Medium' : return (`
    <div>
     <div class="flex items-center space-x-2">
      <div class="h-5 w-5 rounded-full bg-yellow-500"></div>
        <div>Medium</div>
      </div>
    </div>
    `);
    case 'High' : return (`
    <div>
      <div class="flex items-center space-x-2">
        <div class="h-5 w-5 rounded-full bg-orange-500"></div>
        <div>High</div>
        </div>
    </div>
    `);
    case 'Critical' : return (`
     <div>
      <div class="flex items-center space-x-2">
        <div class="h-5 w-5 rounded-full bg-red-600"></div>
        <div>Critical</div>
        </div>
    </div>
    `);
  }
}

function formatDate(date) {
    var d = new Date(date),
    month = '' + (d.getMonth() + 1),
    day = '' + d.getDate(),
    year = d.getFullYear();
    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;
    return [day,month,year].join('-');
}

function getData(id) { 
  return $.ajax({
    url: '/ajax/getUserInfo/',
    type: 'GET',
    data: {
        'id': id,
      }
  })
};

async function getUserInfo(id) {
  let result = null
  try {
    const res = await getData(id)
    result = JSON.parse(res)[0].fields.username
  } catch(err) {
    console.log(err);
  }
  return result
}

function filterSeverity(data) {
  severity = data
  table()

  $("#filterSeverity").empty().append("");

  if(data ===  'Low'){
    $("#filterSeverity").append(`
    <div class="flex items-center space-x-2">
      <div class="h-5 w-5 rounded-full bg-green-700"></div>
      <div class="text-sm font-semibold normal-case">Low</div>
    </div>
    `)
  }
  if(data ===  'Medium'){
    $("#filterSeverity").append(`
    <div class="flex items-center space-x-2">
      <div class="h-5 w-5 rounded-full bg-yellow-500"></div>
      <div class="text-sm font-semibold normal-case">Medium</div>
    </div>
    `)
  }
  if(data ===  'High'){
    $("#filterSeverity").append(`
    <div class="flex items-center space-x-2">
      <div class="h-5 w-5 rounded-full bg-orange-500"></div>
      <div class="text-sm font-semibold normal-case">High</div>
    </div>
    `)
  }
  if(data ===  'Critical'){
    $("#filterSeverity").append(`
    <div class="flex items-center space-x-2">
      <div class="h-5 w-5 rounded-full bg-red-600"></div>
      <div class="text-sm font-semibold normal-case">Critical</div>
    </div>
    `)
  }
}

function filterPerson(data){
  person = data
  table()
  $("#filterPerson").empty().append("");

  if(data ===  2){
    $("#filterPerson").append(`
    <div class="flex space-x-2 items-center">
      <div class="text-[10px] bg-blue-500 w-6 h-6 p-1 rounded-full text-white text-center">WN</div>
      <div class="text-sm font-semibold normal-case">wanee</div>
    </div>
    `)
  }
  if(data ===  3){
    $("#filterPerson").append(`
    <div class="flex space-x-2 items-center">
      <div class="text-[10px] bg-red-500 w-6 h-6 p-1 rounded-full text-white text-center">PS</div>
      <div class="text-sm font-semibold normal-case">plaifah</div>
    </div>
    `)
  }
  if(data ===  4){
    $("#filterPerson").append(`
    <div class="flex space-x-2 items-center">
      <div class="text-[10px] bg-gray-500 w-6 h-6 p-1 rounded-full text-white text-center">US</div>
      <div class="text-sm font-semibold normal-case">unassigned</div>
    </div>
    `)
  }
}

function addAssigneeValue(item){
  assignee_value = item
}

function addReporterValue(item){
  reporter_value = item
}

function addAppValue(item){
  app_value = item
}

function filterSearch(){
  table()
}

function assignToMe(item){
  assignee_value = item
  
  $("#assign").empty().append(""); //unassigned

  if(item === '4'){
    $("#assign").append(` 
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-gray-500 w-6 h-6 p-1 rounded-full text-white text-center">UN</div>
      <button class="text-md" name="person" value="Unassigned">unassigned</button>
    </div>
    `)
  }
  if(item === '3'){
    $("#assign").append(`
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-red-500 w-6 h-6 p-1 rounded-full text-white text-center">PL</div>
      <button class="text-md" name="person" value="Plaifah">plaifah</button>
    </div>
    `)  
  }
  if(item === '2'){
    $("#assign").append(`
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-blue-500 w-6 h-6 p-1 rounded-full text-white text-center">WN</div>
      <button class="text-md" name="person" value="Wanee">wanee</button>
    </div>
    `)  
  }
}

function Assignee(item){
  assignee_value = item
  $("#assign").empty().append(""); //unassigned
  if(item === 4){
    $("#assign").append(` 
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-gray-500 w-6 h-6 p-1 rounded-full text-white text-center">UN</div>
      <button class="text-md" name="person" value="Unassigned">unassigned</button>
    </div>
    `)
  }
  if(item === 3){
    $("#assign").append(`
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-red-500 w-6 h-6 p-1 rounded-full text-white text-center">PL</div>
      <button class="text-md" name="person" value="Plaifah">plaifah</button>
    </div>
    `)  
  }
  if(item === 2){
    $("#assign").append(`
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-blue-500 w-6 h-6 p-1 rounded-full text-white text-center">WN</div>
      <button class="text-md" name="person" value="Wanee">wanee</button>
    </div>
    `)  
  }
}

function Reporter(item) {
  reporter_value = item
  $("#Reporter").empty().append("");

  if(item === 4){
    $("#Reporter").append(`
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-gray-500 w-6 h-6 p-1 rounded-full text-white text-center">UN</div>
      <button class="text-md" name="person" value="Unassigned">unassigned</button>
    </div>
    `)
  }
  if(item === 3){
    $("#Reporter").append(`
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-red-500 w-6 h-6 p-1 rounded-full text-white text-center">PL</div>
      <button class="text-md" name="person" value="Plaifah">plaifah</button>
    </div>
    `)  
  }
  if(item === 2){
    $("#Reporter").append(`
    <div class="flex items-center space-x-2">
      <div class="text-[10px] bg-blue-500 w-6 h-6 p-1 rounded-full text-white text-center">WN</div>
      <button class="text-md" name="person" value="Wanee">wanee</button>
    </div>
    `)  
  }
}

function App(item){
  app_value = item
  $("#app").empty().append("");

  if(item === 'Splunk'){
    $("#app").append(`
      <div class="text-sm">Splunk</div>
    `)
  }

  if(item === 'Special case'){
    $("#app").append(`
      <div class="text-sm">Special case</div>
    `)
  }

}

function submit(){
  $.ajax({
    url: '/ajax/updateJobalertById/',
    cache: false,
    data: {
      jobPk:jobPk,
      app_value:app_value,
      reporter_value:reporter_value,
      assignee_value:assignee_value
    },
    type: 'GET',
    success:async function(data) {
      location.reload();
    }})
}

async function getJobById(ticket_id,pk){
  jobPk= pk
  ticketId = ticket_id
  $("#ticket_id").empty().append("");
  $("#date").empty().append("");
  $("#searchName").empty().append("");
  $("#link").empty().append("");
  $("#severity").empty().append("");
  $("#result").empty().append("");
  $("#get_id").empty().append("");
  $("#ticketId").empty().append("");

  $.ajax({
    url: '/ajax/getJobalertById/',
    data: {
      ticket_id
    },
    type: 'GET',
    success:async function(data) {
      console.log(JSON.parse(data)[0].pk)
      const result = JSON.parse(data)[0].fields

      App(result.app)
      Assignee(result.assign)
      Reporter(result.report)
      $("#ticket_id").append(`<div class="text-lg font-semibold">${result.ticket_id}</div>`)
      $("#date").append(`<div>${formatDate(result.date)}</div>`)
      $("#searchName").append(`<div>${result.search_name}</div>`)
      $("#link").append(`<div>${result.result_link}</div>`)
      $("#severity").append(`<div>${showSeverity(result.severity)}</div>`)
      $("#ticketId").append(`<button class="bg-[#3B82F6] px-2 py-2 rounded-md text-white font-semibold" type="submit" id="ticketId" name="ticketId" value=${JSON.parse(data)[0].pk}>save</button>`)

      for (const [key, value] of Object.entries(JSON.parse(result.results))) {
        $("#result").append(
          `<div class="flex space-x-3">
              <div class="font-semibold">${key}: </div>
              <div>${value}</div>
          </div>`)
      }
    }})
}

function table() {
  input = document.getElementById("search");
  search = input?.value

  $("#jobData").empty().append("");

  $(document).ready(function() {
      $.ajax({
        url: '/ajax/getJobAlert/',
        data:{
          severity,
          person,
          search
        },
        type: 'GET',
        success:async function(data) {
          const result = JSON.parse(data)
          let assignName = null

          for (var i = 0; i < result.length; i++) {
            const items = result[i].fields
            const jobPk = result[i].pk

            await getUserInfo(items.assign).then((value) => {
              assignName = value
            })
 
            $("#jobData").append(`
              <tr>
                <td>${items.ticket_id}</td>
                <td>${formatDate(items.date)}</td>
                <td>${items.search_name}</td>
                <td>${showSeverity(items.severity)}</td>
                <td>${assignName}</td>
                <td>
                  <label for="my-drawer-4">
                    <div class="flex items-center space-x-2 cursor-pointer">
                      <img class="w-5 h-5" src="../static/image/open.png"/>
                      <div class="text-xs" onclick="getJobById(${items.ticket_id},${jobPk})">View Result</div>
                    </div>
                  </label>
                </td>
              </tr>
              `)
          }
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
  });
}

// การเขียนแบบนี้เรียกว่า IIFE คือ จะเป็น function ที่ถูกเรียกเมื่อ app มีการทำงาน
(() =>{
table()
})()