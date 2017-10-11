[%bs.raw {|require('./footer.css')|}];

let component = ReasonReact.statelessComponent "Footer";

let make _children => {  
  {
    ...component,
    render: fun _self =>
      <footer className="footer">
        <h3>(ReasonReact.stringToElement "Footer")</h3>
      </footer>
  }
};