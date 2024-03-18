import React, { useState } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { fetchExtractedText } from '../services/apiService';
import { useNavigate } from 'react-router-dom';
import Loader from './Loader'; // Import the Loader component

const UrlInputForm = () => {
    const [submitError, setSubmitError] = useState('');
    const [isLoading, setIsLoading] = useState(false); // State to track loading status
    const navigate = useNavigate();

    const initialValues = {
        url: '',
    };

    const validationSchema = Yup.object().shape({
        url: Yup.string().url('Invalid URL format').required('URL is required'),
    });

    const handleSubmit = async (values, { setSubmitting }) => {
        setIsLoading(true); // Set loading to true before API call
        console.log("Submitting URL:", values.url);
        setSubmitError('');
        try {
            const data = await fetchExtractedText(values.url);
            console.log("URL submission successful.", data);
            navigate('/results', { state: { extractedText: data } });
        } catch (error) {
            console.error("Error during URL submission:", error);
            setSubmitError(error.message || 'An error occurred. Please try again.');
        } finally {
            setIsLoading(false); // Set loading to false after API call
            setSubmitting(false);
        }
    };

    return (
        <div>
            <Loader isLoading={isLoading} /> {/* Render Loader component and pass isLoading state */}
            <Formik
                initialValues={initialValues}
                validationSchema={validationSchema}
                onSubmit={handleSubmit}
            >
                {({ isSubmitting }) => (
                    <Form>
                        <Field type="text" name="url" placeholder="Enter URL to scrape" />
                        <ErrorMessage name="url" component="div" className="error" />
                        <button type="submit" disabled={isSubmitting || isLoading}>Scrape</button>
                        {/* Disable the button when isLoading is true */}
                    </Form>
                )}
            </Formik>
            {submitError && <div className="error">{submitError}</div>}
        </div>
    );
};

export default UrlInputForm;