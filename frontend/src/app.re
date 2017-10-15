[%bs.raw {|require('./app.css')|}];

external logo : string = "./logo.svg" [@@bs.module];

let component = ReasonReact.statelessComponent "App";

let make ::message _children => {
  ...component,
  render: fun _self =>
    <div className="wrapper">
      <Header title="REASONML"/>
      <main>
        (ReasonReact.stringToElement "hello world")
      </main>
      <Footer/>
    </div>
};
