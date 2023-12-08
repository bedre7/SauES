import axios from "axios";
import { useContext } from "react";
import { ReactNode, createContext, useState } from "react";

interface ISauESContext {
  isActive: {
    encrypt: boolean;
    decrypt: boolean;
  };
  loading: boolean;
  error: string;
  outputText: string;
  timeTaken: string;
  encrypt: (key: string, plainText: string) => void;
  decrypt: (key: string, cipherText: string) => void;
}

export const SauESContext = createContext<ISauESContext>({
  isActive: {
    encrypt: false,
    decrypt: false,
  },
  loading: false,
  error: "",
  outputText: "",
  timeTaken: "",
  encrypt: () => {},
  decrypt: () => {},
} as ISauESContext);

export const useSauESContext = (): ISauESContext => {
  const context = useContext(SauESContext);
  if (!context) {
    throw new Error(
      "useSauESContext must be used within a SauESContextProvider",
    );
  }
  return context;
};

const SauESContextProvider: React.FC<{ children: ReactNode }> = ({
  children,
}): JSX.Element => {
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");
  const [outputText, setOutputText] = useState<string>("");
  const [timeTaken, setTimeTaken] = useState<string>("");
  const [isActive, setIsActive] = useState({
    encrypt: false,
    decrypt: false,
  });

  const encrypt = async (key: string, plainText: string) => {
    try {
      setLoading(true);
      setIsActive(() => ({
        encrypt: true,
        decrypt: false,
      }));

      const {
        data: { cypherText, timeTaken },
      } = await axios.post("http://localhost:5000/encrypt", {
        key,
        plainText,
      });

      setOutputText(cypherText);
      setTimeTaken(timeTaken);
      setError("");
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      if (error?.response?.data?.error) setError(error.response.data.error);
      else setError(error.message);
      setOutputText("");
      setTimeTaken("");
    } finally {
      setLoading(false);
    }
  };

  const decrypt = async (key: string, cipherText: string) => {
    try {
      setLoading(true);
      setIsActive(() => ({
        encrypt: false,
        decrypt: true,
      }));

      const {
        data: { plainText, timeTaken },
      } = await axios.post("http://localhost:5000/decrypt", {
        key,
        cipherText,
      });

      setOutputText(plainText);
      setTimeTaken(timeTaken);
      setError("");
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      if (error?.response?.data?.error) setError(error.response.data.error);
      else setError(error.message);
      setOutputText("");
      setTimeTaken("");
    } finally {
      setLoading(false);
    }
  };

  return (
    <SauESContext.Provider
      value={{
        isActive,
        loading,
        error,
        outputText,
        timeTaken,
        encrypt,
        decrypt,
      }}
    >
      {children}
    </SauESContext.Provider>
  );
};

export default SauESContextProvider;
