function dateTime() {
    document.getElementById("mydate").innerHTML = "Date : " + Date();
}
    /*var d = new Date();
    var day = d.getDate();
    var month = d.getMonth()+1;
    var dstring = new Date().toLocaleTimeString();

    if(day < 10){
        day = "0"+d.getDate();
    }

    if(month < 10){
        month = "0"+eval(d.getMonth()+1);
    }
    document.getElementById('mydate').innerHTML = (dstring+" "+day+"."+month+"."+d.getFullYear()) ;
}*/
function userGreeting() {
    let name = document.getElementById("name").value;
    let mood = document.getElementById("mood").value;
    let text="The Astute Sugar Glider welcomes you "+name+", We\'re glad you are doing"+" "+mood+"!";
    document.getElementById("response").innerHTML = text;
  }
function favoriteNumber() {
    let favnum =Number(document.getElementById("favoritenumber").value);
    switch(favnum) 
    {
        case 1:
            document.getElementById("favresult").innerHTML="henagon";
            break;
        case 2:
            document.getElementById("favresult").innerHTML="digon";
            break;
        case 3:
            document.getElementById("favresult").innerHTML="trigon";
            break;
        case 4:
            document.getElementById("favresult").innerHTML="tetragon";
            break;
        case 5:
            document.getElementById("favresult").innerHTML="pentagon";
            break;
        case 6:
            document.getElementById("favresult").innerHTML="hexagon";
            break;
        case 7:
            document.getElementById("favresult").innerHTML="heptagon";
            break;
        case 8:
            document.getElementById("favresult").innerHTML="octagon";
            break;
        case 9:
            document.getElementById("favresult").innerHTML="ennegon";
            break;
        case 10:
            document.getElementById("favresult").innerHTML="decagon";
            break;
        default:
            document.getElementById("favresult").innerHTML="Please enter a number 1-10";
    }
}
let clicks=0;
let goldieclicks=0;
let pass=false;
let full=false;
function clickTracker()
{
    clicks++;
    document.getElementById('trackerresult').innerHTML=clicks+" pats.";
}
document.getElementById('tracker').addEventListener('click', clickTracker());
function goldielocksClicks()
{
    goldieclicks++;
    switch(goldieclicks)
    {
        case 1:
            document.getElementById('goldieresult').innerHTML="Not enough";
            break;
        case 2:
            document.getElementById('goldieresult').innerHTML="A little more";
            break;
        case 3:
            document.getElementById('goldieresult').innerHTML="Just right!";
            pass=true;
            break;
        case 4:
            document.getElementById('goldieresult').innerHTML="Too much!";
            pass=false;
            full=true;
            break;
    }
}
document.getElementById('goldietracker').addEventListener('click', goldielocksClicks());
function easterEgg()
{
    if(pass)
    {
        document.getElementById('eggresult').innerHTML="Congratulations! You've found the easter egg!";
    }
    else if(full)
    {
        document.getElementById('eggresult').innerHTML="He's too full...";
    }
    else
    {
        document.getElementById('eggresult').innerHTML="He's still hungry...";
    }
}
function reset()
{
    location.reload();
}