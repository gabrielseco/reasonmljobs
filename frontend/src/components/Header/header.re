[%bs.raw {|require('./header.css')|}];

let component = ReasonReact.statelessComponent "Header";

let make ::title _children => {  
  {
    ...component,
    render: fun _self =>
      <header className="header">
        <h3>(ReasonReact.stringToElement title)</h3>
      </header>
  }
};