import Form, { FormType } from "./components/Form";

function App() {
  return (
    <div className="bg-background flex min-h-screen items-center justify-center">
      <div className="min-h-[450px] min-w-[900px] rounded-lg bg-gray-700 p-10 shadow-xl">
        <h2 className="mb-10 cursor-pointer text-center text-4xl font-bold text-primary transition-all hover:text-gray-100">
          SauES🔐
        </h2>
        <div className="flex w-full items-center justify-center space-x-20">
          <Form type={FormType.Encrypt} />
          <Form type={FormType.Decrypt} />
        </div>
      </div>
    </div>
  );
}

export default App;
