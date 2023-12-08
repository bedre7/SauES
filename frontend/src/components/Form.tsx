import { FC, useEffect, useRef, useState } from "react";
import { FaLock, FaLockOpen } from "react-icons/fa";
import { ImSpinner3 } from "react-icons/im";
import { IoTimeOutline } from "react-icons/io5";
import { useSauESContext } from "../context";

export enum FormType {
  Encrypt = "encrypt",
  Decrypt = "decrypt",
}

interface FormProps {
  type: FormType;
}

const Form: FC<FormProps> = ({ type }) => {
  const { isActive, encrypt, decrypt, outputText, error, timeTaken, loading } =
    useSauESContext();
  const [formValues, setFormValues] = useState({
    key: "",
    inputText: "",
  });

  const outputRef = useRef<HTMLTextAreaElement>(null);
  const timerRef = useRef<NodeJS.Timeout | null>(null);
  const [copyButtonText, setCopyButtonText] = useState("Copy");

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (type === FormType.Encrypt) {
      encrypt(formValues.key, formValues.inputText);
    } else {
      decrypt(formValues.key, formValues.inputText);
    }
  };

  const changeHandler = (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>,
  ) => {
    const { id, value } = event.target;

    setFormValues((prev) => ({
      ...prev,
      [id]: value,
    }));
  };

  useEffect(() => {
    return () => {
      if (timerRef.current) {
        const timeout = timerRef.current;
        clearTimeout(timeout);
      }
    };
  }, []);

  const copyToClipboard = () => {
    const text = outputRef.current?.value;
    if (text) {
      navigator.clipboard.writeText(text);
    }
    setCopyButtonText("Copied!");
    if (timerRef.current) {
      clearTimeout(timerRef.current);
    }

    timerRef.current = setTimeout(() => {
      setCopyButtonText("Copy");
    }, 1000);
  };

  return (
    <form className="flex w-full flex-col space-y-4" onSubmit={handleSubmit}>
      <div className="group flex flex-col items-start space-y-2">
        <label
          className="text-sm text-gray-500 transition-all group-focus-within:text-primary"
          htmlFor="key"
        >
          Key for {type}ion (6 characters max)
        </label>
        <input
          id="key"
          type="text"
          value={formValues.key}
          onChange={changeHandler}
          autoComplete="off"
          autoCorrect="off"
          spellCheck="false"
          placeholder="Enter key*"
          className="w-full rounded-md bg-gray-400 p-1.5 text-gray-600 ring-2 ring-gray-300 placeholder:text-gray-500 focus-within:outline-none focus:ring-primary"
        />
      </div>
      <div className="group flex flex-col items-start space-y-2">
        <label
          className="text-sm text-gray-500 transition-all group-focus-within:text-primary"
          htmlFor="inputText"
        >
          Text to {type}
        </label>
        <textarea
          id="inputText"
          onChange={changeHandler}
          value={formValues.inputText}
          placeholder={`Enter text to ${type}*`}
          className="min-h-[100px] w-full rounded-md bg-gray-400 p-1.5 text-sm text-gray-700 ring-2 ring-gray-300 placeholder:text-gray-500 focus-within:outline-none focus:ring-primary"
        />
      </div>
      <button
        className={`w-full rounded-md bg-primary px-4 py-2 text-sm text-gray-100 transition-all hover:bg-secondary focus:outline-none
        ${
          loading && isActive[type]
            ? "cursor-not-allowed opacity-60"
            : "opacity-100"
        }
        `}
        type="submit"
      >
        {loading && isActive[type] ? (
          <ImSpinner3 className="mr-2 inline-block animate-spin" />
        ) : type === FormType.Encrypt ? (
          <FaLock className="mr-2 inline-block" />
        ) : (
          <FaLockOpen className="mr-2 inline-block" />
        )}
        <span>{type} text</span>
      </button>
      {error && isActive[type] ? (
        <p className="text-xs text-red-500">{error}</p>
      ) : (
        <p className="text-xs text-red-500">&nbsp;</p>
      )}
      <div className="group relative w-full">
        <button
          className="right-1 top-1 hidden rounded-md bg-primary px-2 py-1 text-xs text-gray-100 transition-all hover:bg-secondary focus:outline-none group-hover:absolute group-hover:block"
          type="button"
          onClick={copyToClipboard}
        >
          {copyButtonText}
        </button>
        <textarea
          id="output-text"
          readOnly
          ref={outputRef}
          value={isActive[type] ? outputText : ""}
          className="min-h-[100px] w-full rounded-md bg-gray-400 p-1.5 text-sm text-gray-700 ring-2 ring-gray-300 placeholder:text-gray-500 focus-within:outline-none focus:ring-primary"
          placeholder={
            type === FormType.Encrypt ? "Encrypted text" : "Decrypted text"
          }
        />
        {timeTaken && isActive[type] && !error && (
          <div className="fixed">
            <IoTimeOutline className="mr-2 inline-block text-green-500" />
            <span className="text-xs text-green-500">
              {type === FormType.Encrypt ? "Encrypted in " : "Decrypted in "}
              {timeTaken}
            </span>
          </div>
        )}
      </div>
    </form>
  );
};

export default Form;
